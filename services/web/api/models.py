# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.postgres.fields import JSONField

class Analytics(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    call = models.OneToOneField('Calls', models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
    dump = JSONField(blank=True, null=True)  # This field type is a guess.
    analysis = JSONField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'analytics'


class Calls(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    flow = models.ForeignKey('Flows', models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
    language_code = models.CharField(max_length=5)
    type = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    caller_number = models.CharField(max_length=20)
    virtual_number = models.CharField(max_length=20)
    uuid = models.CharField(max_length=50)
    flow_version = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=100)
    intent_context = JSONField(blank=True, null=True)  # This field type is a guess.
    retry_metadata = JSONField(blank=True, null=True)  # This field type is a guess.
    flags_to_eval = JSONField(blank=True, null=True)  # This field type is a guess.
    slot_config = JSONField(blank=True, null=True)  # This field type is a guess.
    metadata = JSONField(blank=True, null=True)  # This field type is a guess.
    intents_info = JSONField(blank=True, null=True)  # This field type is a guess.
    contexts = JSONField(blank=True, null=True)  # This field type is a guess.
    tagger_metadata = JSONField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'calls'
        unique_together = (('client', 'uuid'),)


class CampaignDeployments(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    technology = models.CharField(max_length=50, blank=True, null=True)
    from_number = models.CharField(max_length=50, blank=True, null=True)
    sip_name = models.CharField(max_length=50, blank=True, null=True)
    context = models.CharField(max_length=50, blank=True, null=True)
    stasis_app = models.CharField(max_length=50, blank=True, null=True)
    api_key = models.CharField(max_length=50, blank=True, null=True)
    host = models.CharField(max_length=50, blank=True, null=True)
    port = models.CharField(max_length=50, blank=True, null=True)
    extension = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campaign_deployments'


class CampaignTasks(models.Model):
    uuid = models.UUIDField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    campaign = models.ForeignKey('Campaigns', models.DO_NOTHING, blank=True, null=True)
    parser = models.CharField(max_length=100, blank=True, null=True)
    metadata = JSONField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'campaign_tasks'


class Campaigns(models.Model):
    uuid = models.UUIDField(unique=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey('Clients', models.DO_NOTHING, blank=True, null=True)
    flow = models.ForeignKey('Flows', models.DO_NOTHING, blank=True, null=True)
    deployment = models.ForeignKey(CampaignDeployments, models.DO_NOTHING, blank=True, null=True)
    enabled = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    metadata = JSONField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'campaigns'


class Clients(models.Model):
    uuid = models.UUIDField(unique=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    flow_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'clients'


class ConfigHolders(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    partition = models.IntegerField()
    config_type = models.IntegerField()
    flow_config = models.ForeignKey('FlowConfigs', models.DO_NOTHING, blank=True, null=True)
    config = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_holders'


class Conversations(models.Model):
    uuid = models.UUIDField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    call = models.ForeignKey(Calls, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=20)
    sub_type = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    context = models.CharField(max_length=100, blank=True, null=True)
    audio_path = models.CharField(max_length=255, blank=True, null=True)
    audio_base_path = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    metadata = JSONField(blank=True, null=True)  # This field type is a guess.
    debug_metadata = JSONField(blank=True, null=True)  # This field type is a guess.
    prediction = JSONField(blank=True, null=True)  # This field type is a guess.
    tagger_metadata = JSONField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'conversations'


class FlowConfigs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    flow = models.ForeignKey('Flows', models.DO_NOTHING, blank=True, null=True)
    latest_config = models.BooleanField(blank=True, null=True)
    current_config = models.BooleanField(blank=True, null=True)
    version = models.TextField()
    change_log = models.CharField(max_length=200, blank=True, null=True)
    locked_by = models.CharField(max_length=30, blank=True, null=True)
    actions = models.BinaryField(blank=True, null=True)
    intents = models.BinaryField(blank=True, null=True)
    nls_labels = models.BinaryField(blank=True, null=True)
    states = models.BinaryField(blank=True, null=True)
    transitions = models.BinaryField(blank=True, null=True)
    triggers = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flow_configs'


class Flows(models.Model):
    uuid = models.UUIDField(unique=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'flows'


class Migrations(models.Model):
    id = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'migrations'


class OutboundCalls(models.Model):
    uuid = models.UUIDField(unique=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    campaign = models.ForeignKey(Campaigns, models.DO_NOTHING, blank=True, null=True)
    campaign_task = models.ForeignKey(CampaignTasks, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    caller_number = models.CharField(max_length=20)
    virtual_number = models.CharField(max_length=20)
    metadata = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'outbound_calls'


class QorAdminSettings(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    resource = models.TextField(blank=True, null=True)
    user_id = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qor_admin_settings'


class RiemannTags(models.Model):
    uuid = models.UUIDField(primary_key=True)
    tags = JSONField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'riemann_tags'


class TestFiles(models.Model):
    uuid = models.UUIDField(unique=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    flow_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    flow_version = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=60, blank=True, null=True)
    config = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_files'


class VirtualNumbers(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    flow = models.ForeignKey(Flows, models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    virtual_number = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'virtual_numbers'
