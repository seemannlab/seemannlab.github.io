---
layout: page
title: Research
permalink: /research/
---

# Scientific Publications (peer reviewed)

<div id="publications-container">
{% for pub in site.data.publications_clean %}
  <details>
    <summary><b>{{ pub.title }}</b></summary>

   <p><strong>{{ pub.authors }}</strong><br>
   <em>{{ pub.citation }}</em><br>
   {% if pub.paper_url %}
     <a href="{{ pub.paper_url }}">📄 Paper</a>
   {% endif %}
   {% if pub.pubmed_url %}
     <a href="{{ pub.pubmed_url }}">PubMed</a>
   {% endif %}
   {% if pub.summary %}
     <br>{{ pub.summary }}
   {% endif %}
   </p>
   <hr>
  </details>
{% endfor %}
</div>
