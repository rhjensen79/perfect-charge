# Create Secret
kubectl -n perfect-charge  create secret generic barry --from-literal=barry_meter_id=$BARRY_METER_ID --from-literal=barry_token=$BARRY_TOKEN

# Delete secret
kubectl delete -n perfect-charge secret barry