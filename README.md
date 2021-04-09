# Introduction

This module helps you disable the rarely used Horizon panels. It is currently
tested on Ubuntu with Kolla based deployments only.

# Usage

**You cannot use this module with Kolla provided public images.**

## Kolla

Put these codes into `/etc/kolla/template-overrides.j2` and rebuild Horizon images.

```
{% set horizon_packages_append = ['build-essential', 'python3-dev', 'python3-setuptools', 'python3-wheel'] %}

{% block horizon_footer %}
RUN pip3 --no-cache-dir install git+https://github.com/piricloud/horizon-customization-module.git
{% endblock %}
```

## Kolla Ansible

Put these codes into `/etc/kolla/config/horizon/custom_local_settings` and deploy new images.

```
HORIZON_CONFIG["customization_module"] = "horizon_customization.overrides"
HORIZON_CONFIG["disable_volume_groups_panel"] = True
HORIZON_CONFIG["disable_volume_group_snapshots_panel"] = True
HORIZON_CONFIG["disable_load_balancers_panel"] = True
```

There are 3 options available at the moment.

1. `HORIZON_CONFIG["disable_volume_groups_panel"]` to disable Volume Groups panel.
2. `HORIZON_CONFIG["disable_volume_group_snapshots_panel"]` to disable Volume Group Snapshots panel.
3. `HORIZON_CONFIG["disable_load_balancers_panel"]` to disable Load Balancers panel.

# Contribution

**THIS REPOSITORY DOES NOT ACCEPT PULL REQUESTS**.

# License

[Apache License 2.0](LICENSE)

# Author

This repo is maintained by the [Piri Cloud](mailto:hello@piri.cloud) team.
