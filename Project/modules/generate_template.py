from jinja2 import Environment, FileSystemLoader
import yaml

def get_template(env):
    with open('service-discovery.yaml', 'r') as file:
        svc_conf = yaml.safe_load(file)

    monitoringserver = svc_conf[env]['monitoring-server']
    keystore = svc_conf[env]['key-store']
    webservicefrontend = svc_conf[env]['web-service-frontend']
    dbservicebackend = svc_conf[env]['db-service-backend']

    file_loader = FileSystemLoader('templates')
    jinja_env = Environment(loader=file_loader)
    template = jinja_env.get_template("config.yaml")
    outputText = template.render(
        monitoringserver = monitoringserver,
        keystore = keystore,
        webservicefrontend = webservicefrontend,
        dbservicebackend = dbservicebackend
    )

    f = open(f"output/{env}Config.yaml", "w")
    f.write(outputText)
    f.close()