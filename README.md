[![Build All Containers](https://github.com/rhjensen79/perfect-charge/actions/workflows/build-all.yml/badge.svg)](https://github.com/rhjensen79/perfect-charge/actions/workflows/build-all.yml) 
# Perfect Charge

Note this readme and the app, is still work in progress. So until this line is gone, treat it as such.

## Description

An app, with the purpose,of getting the price of KWH price from [Barry](https://barry.energy/dk), and then schelduling a charge on an [Easee](https://easee.com) charger, when it's below the requested threshold. 

![Grafana](grafana.png)

Design is based on a multi tier k8s app, as described below.
It could be done more simple, but the secondary purpose of this app, is to use it for for demo's for my work.

![image](design.png)

# Installation
## Env Variables

The following enviromental variables, need to be set on the container, and the OS from where you are creating the secrets. , for it to work.
### Value

- BARRY_METER_ID
- BARRY_TOKEN
### Control

- EASEE_USER
- EASEE_PASSWORD

### Log

- GRAFANA_URLS
- GRAFANA_DATABASE
- GRAFANA_TIMEOUT
- GRAFANA_USERNAME
- GRAFANA_PASSWORD 

## Namespace

The app default to the namespace perfect-charge
To create it run :
```
kubectl create ns perfect-charge
```

## Secrets

For the app to work, a couple of secrets files, need to be located in the same Namespace, ad the app.

To easesy create them, make sure your local OS has them set already (with correct values), and you have access to the Kubernetes cluster, where you are going to deploy the app, and run the following commands.

```
kubectl -n perfect-charge  create secret generic barry --from-literal=barry_meter_id=$BARRY_METER_ID --from-literal=barry_token=$BARRY_TOKEN

kubectl -n perfect-charge  create secret generic easee --from-literal=easee_password=$EASEE_PASSWORD --from-literal=easee_user=$EASEE_USER

kubectl -n perfect-charge  create secret generic log --from-literal=grafana_urls=$GRAFANA_URLS --from-literal=grafana_database=$GRAFANA_DATABASE --from-literal=grafana_timeout=$GRAFANA_TIMEOUT --from-literal=grafana_username=$GRAFANA_USERNAME --from-literal=grafana_password=$GRAFANA_PASSWORD
```

If you make a mistake, it's easy to delete a secret again, with the following command.
```
kubectl delete -n perfect-charge secret NameOfSecret
```

## Deploy

To deploy the app, after the prereq is created, simply run
```
kubectl apply -f k8s/perfect-charge-yaml
```
