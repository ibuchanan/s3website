# s3bucket

This is a Python project with CDK
for provisioning a static website hosted on an S3 bucket.

This project is set up like a standard Python project.
To create the virtualenv and install dependencies:

```shell
$ pipenv install
```

After the install process completes
and the virtualenv is created,
you can use the following step to activate your virtualenv.

```shell
$ pipenv shell
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies,
for example other CDK libraries,
just add them with `pipenv install`.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
