# Generated by Django 4.0.5 on 2022-06-27 18:30

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                    "type",
                    models.UUIDField(
                        default=uuid.UUID("37703600-b85a-44a3-9b7c-e19b46822d4b")
                    ),
                ),
                (
                    "action",
                    models.UUIDField(
                        default=uuid.UUID("a9d0e55d-29d2-4025-8a2a-27d5b83b53db")
                    ),
                ),
                (
                    "reviewId",
                    models.UUIDField(
                        default=uuid.UUID("987a87c3-a2a0-469c-a2a3-353e8d1dd555")
                    ),
                ),
                ("content", models.TextField()),
                ("attachedPhotoIds", models.TextField(blank=True)),
                (
                    "userId",
                    models.UUIDField(
                        default=uuid.UUID("674b0bb0-e076-43b7-b1c2-5d0567e2dfde")
                    ),
                ),
                (
                    "placeId",
                    models.UUIDField(
                        default=uuid.UUID("fa86232e-d109-4962-be5a-7fac4bb71eac")
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.UUID("3e4cde66-fd1a-44ac-8f51-493b6d225a22"),
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50)),
                ("country", models.CharField(blank=True, max_length=50)),
                ("region", models.CharField(blank=True, max_length=50)),
                ("address", models.CharField(blank=True, max_length=256)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PlaceHistory",
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
                    "place_id",
                    models.UUIDField(
                        default=uuid.UUID("5f63d825-0a13-49bf-a863-ef08ea4bfb13")
                    ),
                ),
                ("review_total", models.IntegerField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Point",
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
                    "user_id",
                    models.UUIDField(
                        default=uuid.UUID("d6f0181a-38d8-437c-a942-9ea31e5d54aa")
                    ),
                ),
                ("point_total", models.IntegerField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("user_id", models.UUIDField(default=uuid.uuid4)),
                ("place_id", models.UUIDField(default=uuid.uuid4)),
                ("content", models.TextField()),
                ("photo_id", models.TextField(blank=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PointHistory",
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
                    "review_id",
                    models.UUIDField(
                        default=uuid.UUID("c267b47e-a096-4eca-a580-0706dbcc658d")
                    ),
                ),
                ("content_point", models.IntegerField(default=0)),
                ("photo_point", models.IntegerField(default=0)),
                ("start_point", models.IntegerField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "point_id",
                    models.ForeignKey(
                        db_column="point_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mileage.point",
                    ),
                ),
            ],
        ),
    ]
