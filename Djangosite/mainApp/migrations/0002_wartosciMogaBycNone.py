# Generated by Django 4.1.9 on 2023-05-15 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0001_zmianaKlasaAbstrakcyjna"),
    ]

    operations = [
        migrations.AlterField(
            model_name="citationcount",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="citationcount",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="citationcount",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="citationcount",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="citationsperpublication",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="citationsperpublication",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="citationsperpublication",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="citationsperpublication",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="citingpatentscount",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="citingpatentscount",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="citingpatentscount",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="citingpatentscount",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="collaboration",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="collaboration",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="collaboration",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="collaboration",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="collaborationimpact",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="collaborationimpact",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="collaborationimpact",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="collaborationimpact",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="fieldweightedcitationimpact",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="fieldweightedcitationimpact",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="fieldweightedcitationimpact",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="fieldweightedcitationimpact",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="hindices",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="hindices",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="hindices",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="hindices",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="outputsintopcitationpercentiles",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="outputsintopcitationpercentiles",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="outputsintopcitationpercentiles",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="outputsintopcitationpercentiles",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="patentcitationscount",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="patentcitationscount",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="patentcitationscount",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="patentcitationscount",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="patentcitationsperscholarlyoutput",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="patentcitationsperscholarlyoutput",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="patentcitationsperscholarlyoutput",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="patentcitationsperscholarlyoutput",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="patentcitedscholarlyoutput",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="patentcitedscholarlyoutput",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="patentcitedscholarlyoutput",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="patentcitedscholarlyoutput",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="publicationsintopjournalpercentiles",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="publicationsintopjournalpercentiles",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="publicationsintopjournalpercentiles",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="publicationsintopjournalpercentiles",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
        migrations.AlterField(
            model_name="scholarlyoutput",
            name="subjectAreaId",
            field=models.ForeignKey(
                help_text="Id głównej dziedziny naukowej. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.subjectarea",
                verbose_name="Id Dziedzina Naukowej",
            ),
        ),
        migrations.AlterField(
            model_name="scholarlyoutput",
            name="universityId",
            field=models.ForeignKey(
                help_text="Id uczelni. Id opowiada Id z Scival-a",
                on_delete=django.db.models.deletion.CASCADE,
                to="mainApp.university",
                verbose_name="Id Uczelni",
            ),
        ),
        migrations.AlterField(
            model_name="scholarlyoutput",
            name="value",
            field=models.FloatField(
                blank=True,
                help_text="Wartość danej metryki",
                null=True,
                verbose_name="Wartość",
            ),
        ),
        migrations.AlterField(
            model_name="scholarlyoutput",
            name="year",
            field=models.CharField(
                help_text="Rok metryki", max_length=10, verbose_name="Rok"
            ),
        ),
    ]
