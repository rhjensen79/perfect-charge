# Create Secret
kubectl -n perfect-charge  create secret generic barry --from-literal=barry_meter_id=$BARRY_METER_ID --from-literal=barry_token=$BARRY_TOKEN

kubectl -n perfect-charge  create secret generic easee --from-literal=easee_password=$EASEE_PASSWORD --from-literal=easee_user=$EASEE_USER

kubectl -n perfect-charge  create secret generic log --from-literal=grafana_urls=$GRAFANA_URLS --from-literal=grafana_database=$GRAFANA_DATABASE --from-literal=grafana_timeout=$GRAFANA_TIMEOUT --from-literal=grafana_username=$GRAFANA_USERNAME --from-literal=grafana_password=$GRAFANA_PASSWORD

# Delete secret
kubectl delete -n perfect-charge secret barry
kubectl delete -n perfect-charge secret easee

# Create docker registry secret

kubectl create secret docker-registry regcred --docker-server=ghcr.io --docker-username=rhjensen79 --docker-password=password --docker-email=robert@robert-jensen.dk -n perfect-charge