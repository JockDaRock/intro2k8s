# Intro to k8s - App Deployment and resiliency

> Kube - control, kube - C.T.L, kube - cuttle (you know like a cuttle fish)???

## Before we start, let's check we are have the right k8s config context.

* Use kubectl to check your k8s config `kubectl config get-contexts`

If it doesn't look like this... 

![](images/context.png) 

...then we will update the config to use the correct context. `kubectl config use-context devnetuser0X`. Replace the X with the correct number from your context list.


## Deploying Apps

### Deploy Apps - Kubectl commands
 
* Let's standup a basic app.  `kubectl run welcome-app --image=jockdarock/welcome_app:latest --replicas=1`

* We will check to see if our k8s app is running on our cluster.  `kubectl get deployments`

* Now let's see all the info about our deployment.  `kubectl describe deployment welcome-app`

* But wait we can't access our web app yet from our browser.  We need to expose the service on our  `kubectl expose deployment welcome-app --type=LoadBalancer --name=welcome-app --port 5555 --target-port 5555`

* Let's check to see if our service is exposed on to the world on our k8s cluster. `kubectl get services` It's not quite ready yet, but there is a way we can leave it up on the console until it is ready.  `kubectl get services -w`

* Let's also check the logs of our  to see what we see there.  First we need to list our pods. `kubectl get pods` Copy the name of the **welcome-app** pod.

Then type... `kubectl logs welcome-app-<UID>`

* Its great we got our web app running, but what if our pod dies or we want the app to be able to handle a bit more load.  Let's scale our app up.  `kubectl scale --replicas=3 deployment welcome-app`

* Now let's clean up our service and deployments.

`kubectl delete deployment welcome-app`

`kubectl delete service welcome-app`

### Deploy Apps - k8s definition Yaml

* Now that we have seen how to use the base commands to deploy from the command line we can now look at how to define our application from a Yaml definition.

* Let's look at our service yaml`code welcome_app_dply.yml`

* Like before we will create our deployment.  `kubectl create -f welcome_app_dply.yml`

* Now let's look at our service yaml. `code welcome_app_svc.yml`

Now that we understand how we define services in our yaml definition, let's expose our service so we can access our web app.  `kubectl create -f welcome_app_svc.yml`

Now for a bigger more fun application... serverless on kubernetes w/ OpenFaaS

 