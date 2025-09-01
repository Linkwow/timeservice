const core = require('@actions/core')
const github = require('@actions/github')
const exec = require('@actions/exec')

function run() {
    let bucket = core.getInput('bucket', {required: true})
    let region = core.getInput('region', {required: true})
    let folder = core.getInput('folder', {required: true})

    exec.exec('ls ./target/')
    exec.exec(`aws s3 sync ${folder} s3://${bucket} --region ${region}`)

    let s3Url = `http://${bucket}.s3-website-us-east-1.amazonaws.com/`
    core.setOutput('s3-bucket-url', s3Url)
}

run();


