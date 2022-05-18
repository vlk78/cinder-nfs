# Copyright 2021 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import charms_openstack.charm

charms_openstack.charm.use_defaults('charm.default-select-release')


class CinderNFSCharm(
        charms_openstack.charm.CinderStoragePluginCharm):

    name = 'cinder_nfs'
    version_package = 'cinder-common'
    release = 'ocata'
    packages = []
    release_pkg = 'cinder-common'
    stateless = False
    mandatory_config = ['nfs-server-hostname', 'nfs-shares-config',
                        'nfs-mount-point-base', 'volume-backend-name']

    def cinder_configuration(self):
        cget = self.config.get
        volumedriver = 'cinder.volume.drivers.nfs.NfsDriver'
        driver_options_common = [
            ('volume_driver', volumedriver),
            ('volume_backend_name', cget('volume-backend-name')),
            ('nfs_server_hostname', cget('nfs-server-hostname')),
            ('nfs_shares_config', cget('nfs-shares-config')),
            ('nfs_mount_point_base', cget('nfs-mount-point-base')),
        ]

        return (driver_options_common)
