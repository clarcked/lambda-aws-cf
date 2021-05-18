@echo off
set ENV="demo"
set AWS_ACCOUNT="edn"
set AWS_PROFILE="default"
set PRODUCT="ResumenTC"
set OWNER="ExperimentacionNegocio"
set COST_CENTER="99999"
set STACK=%AWS_ACCOUNT%-%ENV%-api-consulta
set BUCKET=%AWS_ACCOUNT%-s3-%ENV%-resumenes-deploys

aws cloudformation delete-stack --stack-name %STACK% --profile %AWS_PROFILE%