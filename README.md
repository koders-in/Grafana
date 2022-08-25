# grafana-exporters

<h1>Grafana</h1> 
<p>Grafana is multi-platform open source analytics and interactive visualization web application. It provides charts, graphs, and alerts for the web when connected to supported data sources. A licensed Grafana Enterprise version with additional capabilities is also available as a self-hosted installation or an account on the Grafana Labs cloud service. It is expandable through a plug-in system. End users can create complex monitoring dashboards using interactive query builders. Grafana is divided into front end and back end, written in TypeScript and Go, respectively.</p>

<h1>Exporter</h1>
<p>Exporters are essential pieces within a Prometheus monitoring environment in which each program acting as a Prometheus client holds an exporter at its core. An exporter is comprised of software features that produce metrics data, and an HTTP server that exposes the generated metrics available via a given endpoint.</p>

<h1>Redmine Dashboard</h1>
<p>Redmine is a free and open source, web-based project management and issue tracking tool. It allows users to manage multiple projects and associated subprojects. It features per project wikis and forums, time tracking, and flexible, role-based access control. It includes a calendar and Gantt charts to aid visual representation of projects and their deadlines. Redmine integrates with various version control systems and includes a repository browser and diff viewer.

The design of Redmine is significantly influenced by Trac, a software package with some similar features.

Redmine is written using the Ruby on Rails framework. It is cross-platform and cross-database and supports 49 languages.</p>

![Redmine](https://user-images.githubusercontent.com/87137729/186405408-6e2cf995-5113-4901-ba61-9409b042ac08.jpg)

<h1>Google Analytics Dashboard</h1>
<p>
Google Analytics is a web analytics service offered by Google that tracks and reports website traffic, currently as a platform inside the Google Marketing Platform brand.Google launched the service in November 2005 after acquiring Urchin.

As of 2019, Google Analytics is the most widely used web analytics service on the web. Google Analytics provides an SDK that allows gathering usage data from iOS and Android app, known as Google Analytics for Mobile Apps.Google Analytics can be blocked by browsers, browser extensions, firewalls and other means.

Google Analytics has undergone many updates since its inception and is currently on its 4th iteration — GA4. GA4 is the default Google Analytics installation, and is the renamed version for the (App + Web) Property that Google released in 2019 in a Beta form. GA4 has also replaced Universal Analytics (UA). One notable feature of GA4 is a natural integration with Google's BigQuery — a feature previously only available with the enterprise GA 360. This move indicates efforts by Google to integrate GA and its free users into their wider cloud offering</p>
![Google Analytics](https://user-images.githubusercontent.com/87137729/186407964-c51afcad-3ea8-433a-8d0a-c2ea03d70c89.jpg)

<h1>Network Exporter</h1>
<p>It has an overview of Port/WiFi data for your Gateway and Access Points, including:

Transmit / Receive
Uptime
Link status and speed
Drop rate and retry (Unifi WiFi)
As well as detailed switch stats for each port, including Unicast, Broadcast and Multicast packets.

Uses Prometheus with the following exporters:

SNMP Exporter
With Grafana variables/constants, you can easily add:

More gateway and switch ports
More radios/Wifi networks </p>
![system-monitoring](https://user-images.githubusercontent.com/68678634/186657268-467e9fc0-77bd-4b27-baf1-d61c887acc59.png)

<h1>Gitub Exporter</h1>
<p>In this we can fetch the data of the github repo's
like some of the data which we can fetch is contributors, no of commits, issues (active, close), pull requests, comments.
  we can fetch the the data using metrics and dimensions available in the github api documentation, then we can code them according to the data which we need from the github and attach that exporter to the prometheus using docker and then use it on grafana display the charts and stats which we need in our github exporter.
</p>

![comment_trends](https://user-images.githubusercontent.com/68678634/186653129-e61accd4-d665-429b-8359-4df72860a306.png)
