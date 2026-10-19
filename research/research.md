---
layout: page
title: Research
permalink: /research/
---

# Scientific Publications (peer reviewed)

<div id="publications-container">
{% for pub in site.data.publications_clean %}
  <div class="publication">
    <h4>{{ pub.title }}</h4>
    <p><strong>{{ pub.authors }}</strong></p>
    <p><em>{{ pub.citation }}</em>
    {% if pub.paper_url %}
      <a href="{{ pub.paper_url }}">📄 Paper</a>
    {% endif %}
    {% if pub.pubmed_url %}
      <a href="{{ pub.pubmed_url }}">PubMed</a>
    {% endif %}
    </p>
  </div>
  <hr>
{% endfor %}
</div>
