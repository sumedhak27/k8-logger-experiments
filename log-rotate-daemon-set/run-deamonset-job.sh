#!/bin/bash

set -euo pipefail

SCRIPT_DIR=$(dirname $0)
echo $SCRIPT_DIR
export KUBECONFIG=/etc/kubernetes/admin.conf

function main() {
  kubectl apply -f $SCRIPT_DIR/daemon/daemonset.yaml
  wait_for_pods log-rotate-daemon
  wait_for_completion log-rotate-daemon
  kubectl delete -f $SCRIPT_DIR/daemon/daemonset.yaml
} 

function wait_for_pods() {
  echo -n "waiting for $1 pods to run"

  PODS=$(kubectl get pods | grep $1 | awk '{print $1}')

  for POD in ${PODS}; do
    while [[ $(kubectl get pod ${POD} -o go-template --template "{{.status.phase}}") != "Running" ]]; do
      sleep 1
      echo -n "."
    done
  done

  echo
}

function wait_for_completion() {
  echo -n "waiting for $1 daemonset to complete"

  PODS=$(kubectl get pods | grep $1 | awk '{print $1}')

  for POD in ${PODS}; do
    while [[ $(kubectl logs ${POD} --tail 1) != "done" ]]; do
      sleep 1
      echo -n "."
    done
  done

  echo
}

main
