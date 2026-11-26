
from decimal import Decimal, InvalidOperation

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from flask_login import current_user

from app import db
from app.models import Product, StockMovement
from app.decorators import roles_required


main = Blueprint("main", __name__)


# DASHBOARD
@main.route("/dashboard")
@roles_required("admin", "warehouse_manager", "employee")
def dashboard():
    return render_template("dashboard.html", user=current_user)


# ADMIN PANEL
@main.route("/admin")
@roles_required("admin")
def admin_panel():
    return "<h1>Administrator access granted.</h1>"


# PRODUCT REGISTRATION
@main.route("/products/new", methods=["GET", "POST"])
@roles_required("admin", "warehouse_manager")
def add_product():

    if request.method == "POST":
        sku = request.form.get("sku", "").strip().upper()
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()

        try:
            quantity = int(request.form.get("quantity", "0"))
            reorder_level = int(request.form.get("reorder_level", "10"))
            unit_price = Decimal(request.form.get("unit_price", "0"))

        except (ValueError, InvalidOperation):
            flash("Please enter valid numeric values.", "danger")
            return redirect(url_for("main.add_product"))

        if not sku or not name:
            flash("SKU and product name are required.", "danger")
            return redirect(url_for("main.add_product"))

        if quantity < 0 or reorder_level < 0 or unit_price < 0:
            flash("Inventory values cannot be negative.", "danger")
            return redirect(url_for("main.add_product"))

        existing_product = Product.query.filter_by(sku=sku).first()

        if existing_product:
            flash("A product with that SKU already exists.", "danger")
            return redirect(url_for("main.add_product"))

        product = Product(
            sku=sku,
            name=name,
            description=description,
            quantity=quantity,
            reorder_level=reorder_level,
            unit_price=unit_price
        )

        db.session.add(product)
        db.session.commit()

        flash("Product registered successfully!", "success")
        return redirect(url_for("main.add_product"))

    return render_template("add_product.html")


# INVENTORY
@main.route("/inventory")
@roles_required("admin", "warehouse_manager", "employee")
def inventory():

    products = Product.query.order_by(Product.name.asc()).all()

    return render_template(
        "inventory.html",
        products=products
    )



# RECEIVE STOCK
@main.route("/stock/receive", methods=["GET", "POST"])
@roles_required("admin", "warehouse_manager", "employee")
def receive_stock():

    if request.method == "POST":

        product_id = request.form.get("product_id", type=int)
        reference = request.form.get("reference", "").strip().upper()
        notes = request.form.get("notes", "").strip()
        quantity = request.form.get("quantity", type=int)

        if not product_id or not quantity or quantity <= 0:
            flash("Select a product and enter a positive quantity.", "danger")
            return redirect(url_for("main.receive_stock"))

        if not reference or len(reference) > 100:
            flash("A valid receipt reference is required.", "danger")
            return redirect(url_for("main.receive_stock"))

        if len(notes) > 2000:
            flash("Notes cannot exceed 2000 characters.", "danger")
            return redirect(url_for("main.receive_stock"))

        try:
            product = db.session.get(Product, product_id)

            if not product or not product.is_active:
                flash("Product not found or inactive.", "danger")
                return redirect(url_for("main.receive_stock"))

            existing_movement = StockMovement.query.filter_by(
                product_id=product.id,
                movement_type="RECEIVE",
                reference=reference
            ).first()

            if existing_movement:
                flash(
                    "This receipt reference has already been used for this product.",
                    "danger"
                )
                return redirect(url_for("main.receive_stock"))

            product.quantity += quantity

            movement = StockMovement(
                product_id=product.id,
                user_id=current_user.id,
                movement_type="RECEIVE",
                quantity=quantity,
                reference=reference,
                notes=notes
            )

            db.session.add(movement)
            db.session.commit()

            flash("Stock received successfully!", "success")

        except Exception:
            db.session.rollback()
            flash(
                "Stock receiving failed. No changes were saved.",
                "danger"
            )

        return redirect(url_for("main.inventory"))

    products = Product.query.filter_by(is_active=True).order_by(
        Product.name.asc()
    ).all()

    return render_template(
        "receive_stock.html",
        products=products
    )





# ISSUE STOCK
@main.route("/stock/issue", methods=["GET", "POST"])
@roles_required("admin", "warehouse_manager", "employee")
def issue_stock():

    if request.method == "POST":

        product_id = request.form.get("product_id", type=int)
        reference = request.form.get("reference", "").strip().upper()
        notes = request.form.get("notes", "").strip()
        quantity = request.form.get("quantity", type=int)

        if not product_id or not quantity or quantity <= 0:
            flash("Select a product and enter a positive quantity.", "danger")
            return redirect(url_for("main.issue_stock"))

        if not reference or len(reference) > 100:
            flash("A valid issue reference is required.", "danger")
            return redirect(url_for("main.issue_stock"))

        if len(notes) > 2000:
            flash("Notes cannot exceed 2000 characters.", "danger")
            return redirect(url_for("main.issue_stock"))

        try:
            product = db.session.get(Product, product_id)

            if not product or not product.is_active:
                flash("Product not found or inactive.", "danger")
                return redirect(url_for("main.issue_stock"))

            existing_movement = StockMovement.query.filter_by(
                product_id=product.id,
                movement_type="ISSUE",
                reference=reference
            ).first()

            if existing_movement:
                flash(
                    "This issue reference has already been used for this product.",
                    "danger"
                )
                return redirect(url_for("main.issue_stock"))

            if quantity > product.quantity:
                flash(
                    f"Insufficient stock. Available quantity: {product.quantity}.",
                    "danger"
                )
                return redirect(url_for("main.issue_stock"))

            product.quantity -= quantity

            movement = StockMovement(
                product_id=product.id,
                user_id=current_user.id,
                movement_type="ISSUE",
                quantity=quantity,
                reference=reference,
                notes=notes
            )

            db.session.add(movement)
            db.session.commit()

            flash("Stock issued successfully!", "success")

        except Exception:
            db.session.rollback()
            flash(
                "Stock issuing failed. No changes were saved.",
                "danger"
            )

        return redirect(url_for("main.inventory"))

    products = Product.query.filter_by(is_active=True).order_by(
        Product.name.asc()
    ).all()

    return render_template(
        "issue_stock.html",
        products=products
    )



# STOCK MOVEMENT HISTORY
@main.route("/stock/history")
@roles_required("admin", "warehouse_manager")
def stock_history():

    movements = StockMovement.query.order_by(
        StockMovement.created_at.desc(),
        StockMovement.id.desc()
    ).all()

    return render_template(
        "stock_history.html",
        movements=movements
    )

    
