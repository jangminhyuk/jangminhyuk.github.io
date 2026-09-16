---
layout: research-site
title: "Publications"
permalink: /publications/
---
<header class="index-heading"><h1>Publications</h1><p class="small-note">* Equal contribution · <a href="{{ site.author.googlescholar }}">Google Scholar ↗</a></p></header>
<div class="publication-list">{% for paper in site.data.research %}{% include publication-entry.html item=paper %}{% endfor %}</div>
