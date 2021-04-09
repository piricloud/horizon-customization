# Copyright (c) 2021 Piri Cloud
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import horizon

from django.utils.translation import ugettext_lazy as _
from openstack_dashboard import exceptions
from openstack_dashboard.settings import HORIZON_CONFIG

project_dashboard = horizon.get_dashboard("project")

if HORIZON_CONFIG["disable_volume_groups_panel"]:
    volume_groups_panel = project_dashboard.get_panel("volume_groups")
    project_dashboard.unregister(volume_groups_panel.__class__)

if HORIZON_CONFIG["disable_volume_group_snapshots_panel"]:
    volume_group_snapshots_panel = project_dashboard.get_panel("vg_snapshots")
    project_dashboard.unregister(volume_group_snapshots_panel.__class__)

if HORIZON_CONFIG["disable_load_balancers_panel"]:
    load_balancers_panel = project_dashboard.get_panel("load_balancer")
    project_dashboard.unregister(load_balancers_panel.__class__)
