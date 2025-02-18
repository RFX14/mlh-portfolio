"""empty message

Revision ID: 4130f9d4c366
Revises: 
Create Date: 2021-06-30 20:09:16.661406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4130f9d4c366"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
