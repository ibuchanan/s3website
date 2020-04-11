#!/usr/bin/env python3

from aws_cdk import core

from s3website.s3website_stack import S3WebsiteStack


app = core.App()
S3WebsiteStack(app, "s3website")

app.synth()
