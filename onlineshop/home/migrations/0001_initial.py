# Generated by Django 2.0.1 on 2018-01-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cate_id', models.AutoField(primary_key=True, serialize=False)),
                ('cate_parent_id', models.IntegerField(blank=True, null=True)),
                ('cate_name', models.TextField(blank=True, null=True)),
                ('cate_description', models.TextField(blank=True, null=True)),
                ('cate_status', models.NullBooleanField()),
            ],
            options={
                'db_table': 'Category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
                ('action_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('ship_name', models.TextField(blank=True, null=True)),
                ('ship_address', models.TextField(blank=True, null=True)),
                ('ship_phone', models.TextField(blank=True, null=True)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('total_amount', models.TextField(blank=True, null=True)),
                ('order_status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(blank=True, null=True)),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('product_price', models.TextField(blank=True, null=True)),
                ('product_quantity', models.IntegerField(blank=True, null=True)),
                ('amount', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Order_Detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('cate_id', models.IntegerField(blank=True, null=True)),
                ('product_name', models.TextField(blank=True, null=True)),
                ('product_price', models.TextField(blank=True, null=True)),
                ('product_quantity', models.IntegerField(blank=True, null=True)),
                ('product_image', models.TextField(blank=True, null=True)),
                ('product_detail', models.TextField(blank=True, null=True)),
                ('product_status', models.NullBooleanField()),
            ],
            options={
                'db_table': 'Product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('image_path', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Product_Image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('promotion_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('discount', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Promotion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
            ],
        ),
    ]
