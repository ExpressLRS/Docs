![Banner](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/banner.png)


<center>

[![License](https://img.shields.io/github/license/ExpressLRS/Docs?style=flat-square)](https://github.com/ExpressLRS/Docs/blob/master/LICENSE)
[![Chat](https://img.shields.io/discord/596350022191415318?color=%235865F2&logo=discord&logoColor=%23FFFFFF&style=flat-square)](https://discord.gg/expresslrs)
[![Build Status](https://img.shields.io/github/actions/workflow/status/ExpressLRS/Docs/publish.yml?logo=github&style=flat-square)](https://github.com/ExpressLRS/Docs/actions)

</center>

# ExpressLRS.org Documentation Repository

## Community
We have both a [Discord Server](https://discord.gg/expresslrs) and [Facebook Group](https://www.facebook.com/groups/636441730280366), which have great support for new users and constant ongoing development discussion

## Support ExpressLRS
You can support ExpressLRS by contributing code, testing new features, sharing your ideas, or helping others get started. We are exceptionally grateful for those who donate their time to our passion.

If you don't have time to lend a hand in that way but still want to have an impact, consider donating. Donations are used for infrastructure costs and to buy test equipment needed to further the project and make it securely accessible. ExpressLRS accepts donations through Open Collective, which provides recognition of donors and transparency on how that support is utilized.

[![Open Collective backers](https://img.shields.io/opencollective/backers/expresslrs?label=Open%20Collective%20backers&style=flat-square)](https://opencollective.com/expresslrs)


## Installation

You need to have [docker](https://docs.docker.com/engine/install/)
and [docker-compose](https://docs.docker.com/compose/install/) installed in your environment.

If you edit the docs in vscode when you open the top level directory it will ask if you wish to `Reopen in Container` click that button and vscode will automatically run `docker compose up` which will then start serving the documentation as below, otherwise you can do it manually as below.

Then you need to build your container:

```
docker compose build
```

and start mkdocs server:

```
docker compose up
```

After server is running visit [http://localhost:8000/](http://localhost:8000/).

![](https://raw.githubusercontent.com/ExpressLRS/ExpressLRS-Hardware/master/img/community.png)
