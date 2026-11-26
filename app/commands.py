
import click

from app import db
from app.models import User


def register_commands(app):

    @app.cli.command("create-user")
    def create_user():
        """Create a SecureWarehouse user account."""

        username = click.prompt("Username").strip()
        email = click.prompt("Email address").strip().lower()

        role = click.prompt(
            "User role",
            type=click.Choice(
                ["admin", "warehouse_manager", "employee"],
                case_sensitive=False
            ),
            default="employee"
        )

        if not username or not email:
            raise click.ClickException("Username and email are required.")

        existing_user = User.query.filter(
            (User.username == username) |
            (User.email == email)
        ).first()

        if existing_user:
            raise click.ClickException(
                "That username or email is already registered."
            )

        password = click.prompt(
            "Password",
            hide_input=True,
            confirmation_prompt=True
        )

        if len(password) < 12:
            raise click.ClickException(
                "Password must contain at least 12 characters."
            )

        user = User(
            username=username,
            email=email,
            role=role.lower()
        )

        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        click.echo(f"User '{username}' created successfully.")
