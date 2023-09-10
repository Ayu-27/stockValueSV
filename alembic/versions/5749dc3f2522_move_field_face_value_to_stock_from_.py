"""Move field 'face_value' to Stock from FinancialData model

Revision ID: 5749dc3f2522
Revises: c329cf028056
Create Date: 2023-09-07 18:23:08.396731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5749dc3f2522'
down_revision = 'c329cf028056'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('financial_data', 'face_value')
    op.add_column('stocks', sa.Column('face_value', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stocks', 'face_value')
    op.add_column('financial_data', sa.Column('face_value', sa.FLOAT(), nullable=True))
    # ### end Alembic commands ###