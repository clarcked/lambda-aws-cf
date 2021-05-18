@echo off
set ENV="demo"
set AWS_ACCOUNT="edn"
set AWS_PROFILE="default"
set PRODUCT="ResumenTC"
set OWNER="ExperimentacionNegocio"
set COST_CENTER="99999"
set STACK=%AWS_ACCOUNT%-%ENV%-api-consulta
set BUCKET=%AWS_ACCOUNT%-s3-%ENV%-resumenes-deploys
@REM set BUCKET="spvresumen"

@REM sam validate --template "%cd%/cloudf/template.yaml" --profile %AWS_PROFILE%  
sam build --template "%cd%/cloudf/template.yaml" --profile %AWS_PROFILE% && sam deploy --debug --template "%cd%/.aws-sam/build/template.yaml" --stack-name %STACK% --s3-bucket=%BUCKET% --profile %AWS_PROFILE% --capabilities CAPABILITY_NAMED_IAM --parameter-overrides Environment=%ENV% Account=%AWS_ACCOUNT% --tags Environment=%ENV% ProductName=%PRODUCT% Owner=%OWNER% CostCenter=%COST_CENTER%