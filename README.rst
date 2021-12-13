==========================
Clash Configuration Merger
==========================

Download Clash configuration YAML and add local overrides into it.

If you're subscribing to one or more proxy providers, the clash configurations
they provide may contain settings you want to override (e.g. listen port, log-level, etc)
or miss settings you want to specify (e.g. ui, socks port, etc). This project may help by
merging local overrides into the downloaded configuration file to form the final
clash ``config.yaml``.

Features
========

- ✌️ shallow merging for top-level configurations (since 0.1.0)

Install
=======

.. TBD

Development
===========


TODO
====

- systemd-based installer
- documentation
- post-merge actions





