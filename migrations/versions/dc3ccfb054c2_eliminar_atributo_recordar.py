"""Eliminar atributo recordar

Revision ID: dc3ccfb054c2
Revises: ec426f869334
Create Date: 2024-03-11 23:16:04.121416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc3ccfb054c2'
down_revision = 'ec426f869334'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('registro_tareas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'usuarios', ['usuario_id'], ['id'])
        batch_op.drop_column('recordar')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('registro_tareas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('recordar', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('usuario_id')

    # ### end Alembic commands ###
