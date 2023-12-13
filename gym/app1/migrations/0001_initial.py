# Generated by Django 4.2.7 on 2023-12-12 05:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Agreement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="bodybuilders",
            fields=[
                ("firstname", models.CharField(max_length=10)),
                ("lastname", models.CharField(max_length=10)),
                (
                    "gender",
                    models.CharField(
                        choices=[("FM", "Female"), ("ML", "Male")],
                        default="FM",
                        max_length=2,
                    ),
                ),
                ("height", models.PositiveSmallIntegerField()),
                ("weight", models.PositiveSmallIntegerField()),
                (
                    "nationalcode",
                    models.PositiveSmallIntegerField(primary_key=True, serialize=False),
                ),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=15)),
                ("phonenumber", models.PositiveSmallIntegerField()),
                ("aim", models.TextField()),
                ("illness", models.TextField()),
                ("birthdate", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="damages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body_part", models.CharField(max_length=10)),
                ("what", models.CharField(max_length=100)),
                (
                    "when",
                    models.CharField(
                        choices=[("RM", " ماه های اخیر"), ("E", "قبلتر")],
                        default="E",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Gyms",
            fields=[
                (
                    "name",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("manager_name", models.CharField(max_length=20, unique=True)),
                ("manager_cv", models.TextField()),
                ("manager_password", models.CharField(max_length=15)),
                ("facilities", models.TextField()),
                ("capacity", models.PositiveSmallIntegerField()),
                ("numberofmachines", models.IntegerField()),
                ("foundationdate", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                ("phonenumber", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="movements",
            fields=[
                (
                    "name",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("machine_name", models.CharField(max_length=10)),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="program",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("finish_date", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="work_times",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("SHA", "Sanbe"),
                            ("1SH", "1shanbe"),
                            ("2SH", "2shanbe"),
                            ("3SH", "3shanbe"),
                            ("4SH", "4shanbe"),
                            ("5SH", "5shanbe"),
                            ("JOM", "Jomee"),
                        ],
                        max_length=10,
                    ),
                ),
                ("start", models.TimeField()),
                ("end", models.TimeField()),
                (
                    "coach_crew",
                    models.CharField(
                        choices=[("CO", "coach"), ("CR", "crew")], max_length=2
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="workers",
            fields=[
                (
                    "nationalcode",
                    models.PositiveSmallIntegerField(primary_key=True, serialize=False),
                ),
                ("firstname", models.CharField(max_length=10)),
                ("lastname", models.CharField(max_length=10)),
                (
                    "gender",
                    models.CharField(
                        choices=[("FM", "Female"), ("ML", "Male")],
                        default="FM",
                        max_length=2,
                    ),
                ),
                ("password", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="coaches",
            fields=[
                (
                    "workers_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="app1.workers",
                    ),
                ),
                ("sport_degree", models.TextField()),
                ("experience", models.TextField()),
            ],
            bases=("app1.workers",),
        ),
        migrations.CreateModel(
            name="Manager_CustomUser",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "gym_name",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("password", models.PositiveSmallIntegerField()),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
    ]