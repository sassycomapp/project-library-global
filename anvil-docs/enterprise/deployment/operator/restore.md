---
document: "Cluster Restore"
title: "Cluster Restore"
url: "/docs/enterprise/deployment/operator/restore"
doc-id: restore
state: Live
date-created: 2026-09-08
---


# [Cluster Restore](#cluster-restore)

In its default configuration, the Anvil Operator will back up your Anvil Cluster every 24 hours, with the internal databases backed up continuously. You can restore your cluster to any previous time by creating a `ClusterRestore` Resource. For example:

```yaml
apiVersion: anvil.works/v1
kind: ClusterRestore
metadata:
  namespace: anvil
  name: maple-restore
spec:
  targetTime: "2025-04-28T12:00:00Z"
  source:
    pvc:
      claimName: anvil-maple-backup-b7fbaf
```

## [Configuration Reference](#configuration-reference)

#### replaceClusterName

Default: `null`

The name of the cluster to restore to. If not specified, the original name of the backed-up cluster will be used.

#### encryptionKeySecretName

Default: `null`

The name of a Secret containing an encryption key to use for the restore. If not specified, the encryption key name from the backed-up cluster will be used.

#### suffixToken

Default: `null`

The restored resource names have a suffix token to ensure they’re unique. If not specified, this will be the last 6 characters of the Restore resource’s UID.

#### imagePullSecretName

Default: `"anvil-registry-creds"`

The name of a [`kubernetes.io/dockerconfigjson` Secret](https://kubernetes.io/docs/concepts/configuration/secret/#docker-config-secrets) to be used when pulling images from the Anvil container registry.

If not set, the default name can be overridden by the `ANVIL_IMAGE_PULL_SECRET` environment variable or the `imagePullSecret` Helm chart value.

#### imagePrefix

Default: `null`

If set, this overrides the default container image prefix for `imagePrefixPublic` and `imagePrefixPrivate`.

#### imagePrefixPublic

Default: `"anvil.works/public/"`

The prefix to use for public Anvil container images. If not specified, `imagePrefix` is used. If that isn’t set either, `"anvil.works/public/"` is used.

#### imagePrefixPrivate

Default: `"anvil.works/on-site/"`

The prefix to use for private Anvil container images. If not specified, `imagePrefix` is used. If that isn’t set either, `"anvil.works/on-site/"` is used.

#### platformServerVersionTag

Default: `"latest"`

The version of the temporary platform server container used to restore the app source code.

#### busyboxImage

Default: `"busybox"`

The Busybox image to use for init containers.

#### sshServerImage

Default: `"linuxserver/openssh-server"`

The OpenSSH server image to use for SSH servers.

#### targetTime

Default: `"latest_backup"`

The restore point for the cluster. This can be a timezone-aware ISO 8601 timestamp, or `latest_backup` to restore to the most recent backup operation.

Since the database WALs are continuously archived between backups using [PostgreSQL Continuous Archiving](https://www.postgresql.org/docs/10/continuous-archiving.html), you can restore to a more recent time than `latest_backup` by specifying an exact timestamp.

#### defaultStorageClass

Default: `null`

Override the default storage class to use for restored PVCs.

#### replaceClusterSpec

Default: `{}`

Items to merge into the cluster spec of the restored cluster.

## [Restore Source](#restore-source)

Configure the location of the backups to restore from. This is one of:

-   `s3`: Restore from an S3 bucket. Currently this is only possible when running in an AWS EKS cluster.
-   `ssh`: Restore from a remote server via SSH.
-   `nfs`: Restore from an NFS volume in the cluster.
-   `pvc`: Restore from a PVC in the cluster.

### source.s3

#### source.s3.bucketName

Required

The name of the S3 bucket to restore from.

#### source.s3.pathPrefix

Default: `"/"`

The directory in the S3 bucket used to store the backup files.

### source.ssh

#### source.ssh.hostname

Required

The hostname of the SSH server to restore from.

#### source.ssh.port

Default: `22`

The port of the SSH server.

#### source.ssh.directory

Required

The directory on the remote server used to store the backup files.

#### source.ssh.username

Default: `"anvil-restore"`

The username to use for the SSH connection.

#### source.ssh.authSecretName

Required

The name of a [kubernetes.io/ssh-auth Secret](https://kubernetes.io/docs/concepts/configuration/secret/#ssh-authentication-secrets) containing an SSH private key to use for the restore.

#### source.ssh.knownHostsSecretName

Required

The name of an Opaque Secret containing a known hosts file entry for the SSH server.

For example, you could create the following Secret and use it with `knownHostsSecretName: my-known-hosts`:

```bash
kubectl create -n anvil secret generic my-known-hosts --from-file="known_hosts"
```

### source.nfs

#### source.nfs.server

Required

The hostname of the NFS server.

#### source.nfs.export

Required

The exported directory on the NFS server.

#### source.nfs.directory

Default: `"/"`

The subdirectory inside the NFS export used to store the backup files.

### source.pvc

#### source.pvc.claimName

Required

The name of the PVC to use for the restore.

#### source.pvc.directory

Default: `"/"`

The directory in the PVC used to store the backup files.

## [Pods](#pods)

Configure the Kubernetes pods used to restore the cluster.

Each pod definition has a `resources` and `affinity` field. If neither of these are specified for a pod, the top-level `pods.resources` and `pods.affinity` will be used.

For example, the following specifies a 2GiB memory request for the containers in the `restoreServer` pod, but uses a 1GiB request for the containers in all other pods:

```yaml
pods:
  resources:
    requests:
      memory: 1Gi
  restoreServer:
    resources:
      requests:
        memory: 2Gi
```

### pods.resources

Configure the resources requests and limits for the containers in the pod. See the [Kubernetes Resource Management documentation](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) for more information.

#### pods.resources.requests

Default: `null`

#### pods.resources.limits

Default: `null`

### pods.affinity

#### pods.affinity.node

Default: `null`

Configure the node affinity for the pod by specifying a dictionary of keys and values to be used as `requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms`.

For example, the following specifies that the pod must be scheduled on `anvil-node-0`:

```yaml
pods:
  affinity:
    node:
      kubernetes.io/hostname: anvil-node-0
```

See the [Kubernetes Node Affinity documentation](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#node-affinity) for more information.

#### pods.affinity.pod

Default: `null`

Configure the pod affinity for the pod by specifying a dictionary of keys and values to be used as `requiredDuringSchedulingIgnoredDuringExecution.labelSelector`s.

For example, the following specifies that the pod must be scheduled on the same node as any pods with the label `foo=bar`:

```yaml
pods:
  affinity:
    pod:
      foo: bar
```

See the [Kubernetes Pod Affinity documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) for more information.

### pods.restoreServer

Pod configuration (`resources` and `affinity`) for the SSH server used during the restore.

### pods.gitRestore

Pod configuration (`resources` and `affinity`) for restoring the git repository.

### pods.databaseRestore

Pod configuration (`resources` and `affinity`) for restoring the databases.
