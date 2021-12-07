# Perfect Charge

An app, with the purpose,of getting the price of power, and then schelduling it on the charger.

Design will be based on a multi tier k8s app, as described below.

![image](design.png)


## Env Variables

The following enviromental variables, need to be set on the container, for it to work.


### Value
BARRY METER

BARRY_TOKEN


### Control

### Monitoring


sed -i "s|image: ghcr.io/rhjensen79/perfect-charge/value|image: ghcr.io/rhjensen79/perfect-charge/value:latest|" k8s-deployment.yaml