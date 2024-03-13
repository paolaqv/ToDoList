"""Initial migration.

Revision ID: 848553608089
Revises: 
Create Date: 2024-03-11 01:53:35.001088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '848553608089'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('estados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('registro_tareas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=False),
    sa.Column('fecha_inicio', sa.DateTime(), nullable=True),
    sa.Column('fecha_fin', sa.DateTime(), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.Column('estado_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id'], ),
    sa.ForeignKeyConstraint(['estado_id'], ['estados.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('registro_tarea')
    op.drop_table('usuario')
    op.drop_table('estado')
    op.drop_table('categoria')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoria',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('categoria_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('nombre_categoria', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='categoria_pkey'),
    sa.UniqueConstraint('nombre_categoria', name='categoria_nombre_categoria_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('estado',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('estado_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('status', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='estado_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('usuario',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('usuario_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='usuario_pkey'),
    sa.UniqueConstraint('username', name='usuario_username_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('registro_tarea',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('categoria_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('estado_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('descripcion', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('fecha_inicio', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('fecha_fin', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('fecha_creacion', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['categoria_id'], ['categoria.id'], name='registro_tarea_categoria_id_fkey'),
    sa.ForeignKeyConstraint(['estado_id'], ['estado.id'], name='registro_tarea_estado_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['usuario.id'], name='registro_tarea_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='registro_tarea_pkey')
    )
    op.drop_table('registro_tareas')
    op.drop_table('usuarios')
    op.drop_table('estados')
    op.drop_table('categorias')
    # ### end Alembic commands ###
