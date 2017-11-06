'''
Publish tasks and helpers
'''
from invoke import task

from log_utils import logging
from publishing.s3publisher import publish_to_s3

from .common import SITE_BUILD_DIR_PATH


LOGGER = logging.getLogger('PUBLISH')


@task
def publish(ctx, base_url, site_prefix, bucket, cache_control,
            aws_region, access_key_id, secret_access_key,
            dry_run=False):
    '''
    Publish the built site to S3
    '''
    LOGGER.info('Publishing to S3')

    publish_to_s3(
        directory=SITE_BUILD_DIR_PATH,
        base_url=base_url,
        site_prefix=site_prefix,
        bucket=bucket,
        cache_control=cache_control,
        aws_region=aws_region,
        access_key_id=access_key_id,
        secret_access_key=secret_access_key,
        dry_run=dry_run
    )