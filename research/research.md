---
layout: page
title: Research
permalink: /research/
---

My research focuses on the molecular structure and functionality of - specifically non-protein coding - RNA molecules. I am fascinated about the seemingly unlimited applications these molecules may have in bacterial systems and in human health. As a bioinformatician I have developed numerous highly used bioinformatics software, such as PETfold, RNAsnp, and CRISPRroots, and analysed large data related to RNA, RNA interactomes, and transcriptomes in vertebrates, viruses, and bacteria. I discovered thousands of conserved RNA structures in vertebrates which have been systematically overlooked due to low sequence conservation and low expression, which are accessible through the RNAcentral database and have been targeted for de novo lncRNA gene annotation in GENCODE v47. Lately a main focus has been on Bacillus and cyanobacteria allowing me to go much deeper into the mechanistic of RNA-based regulation. In recent investigations we described the stress responses of cyanobacteria under growth-inhibiting high CO₂ levels and the large potential of unexplored non-coding RNAs as regulators for stress adaptation.

<div id="pubs"></div>
<script>
  fetch('/_data/publications_clean.json')
    .then(r => r.json())
    .then(data => {
      const html = data.map(p => `
        <div class="publication">
          <h4>${p.title}</h4>
          <p><strong>${p.authors}</strong></p>
          <p>${p.citation}</p>
          <p>
            ${p.pubmed_url ? `<a href="${p.pubmed_url}">PubMed</a>` : ''}
            ${p.paper_url ? `<a href="${p.paper_url}">Paper</a>` : ''}
          </p>
        </div>
      `).join('');
      document.getElementById('pubs').innerHTML = html;
    });
</script>
