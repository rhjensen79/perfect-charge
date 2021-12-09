# Create Secret
kubectl -n perfect-charge  create secret generic barry --from-literal=barry_meter_id=$BARRY_METER_ID --from-literal=barry_token=$BARRY_TOKEN

# Delete secret
kubectl delete -n perfect-charge secret barry

# Create docker registry secret

kubectl create secret docker-registry regcred --docker-server=ghcr.io --docker-username=rhjensen79 --docker-password=password --docker-email=robert@robert-jensen.dk -n perfect-charge