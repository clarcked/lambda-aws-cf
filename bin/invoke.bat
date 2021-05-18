@echo off
set ENV="demo"
set AWS_ACCOUNT="edn"
set AWS_PROFILE="default"
set PRODUCT="ResumenTC"
set OWNER="ExperimentacionNegocio"
set COST_CENTER="99999"
set STACK=%AWS_ACCOUNT%-%ENV%-api-consulta
@REM set BUCKET=%AWS_ACCOUNT%-s3-%ENV%-resumenes-deploys
set BUCKET="spvresumen"


sam build --template "%cd%/cloudf/template.yaml" --profile %AWS_PROFILE% --use-container && sam local invoke --profile %AWS_PROFILE% --event %cd%/events/test.json