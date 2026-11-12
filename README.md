<!--
ARTWORK PALETTE
Edit ACTIVE_PALETTE near the top of generate_assets.py.
Run python generate_assets.py and commit the updated assets/ folder.
-->


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/nameplate-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/nameplate-light.svg">
  <img src="./assets/nameplate-light.svg" alt="Sarthak Rathi" width="100%">
</picture>

<p>
  <strong>Building software and ML systems.</strong>
</p>

<p>I’m a final-year Computer Science student at Ashoka University. I work across ML evaluation, data infrastructure, and software tools, with an interest in AI security and auditing.</p>

<p>
  <em>B.Sc. Computer Science · Astronomy &amp; Entrepreneurship concentrations · May 2027</em>
</p>

<p>
  <a href="#selected-work">Selected work</a> · <a href="#more-projects">More projects</a> · <a href="#experience">Experience</a> · <a href="#tools-i-work-with">Tools</a> · <a href="#connect">Connect</a>
</p>

<blockquote>
  <p>Currently contributing to the SciCommons research feed with Prof. Suresh Krishna at McGill. <a href="https://feed.scicommons.org/scicommons/default">Explore the public feed</a>
  </p>
</blockquote>

## Selected work

<table width="100%">
  <tbody>
    <tr>
      <td rowspan="2" width="50%">
        <a href="https://github.com/ironLegion88/fkg-graphql-layer/tree/sprint-2/cytoscape">
          <picture>
            <source media="(prefers-color-scheme: dark)" srcset="./assets/ifkg-dark.svg">
            <source media="(prefers-color-scheme: light)" srcset="./assets/ifkg-light.svg">
            <img src="./assets/ifkg-light.svg" alt="Food Knowledge Graph. RDF and a slightly tilted GraphQL block." width="100%">
          </picture>
        </a>
        <h3>Food Knowledge Graph</h3>
        <p>A GraphQL prototype with query depth, complexity, and result limits. Comparing GraphDB and Oxigraph on 14 semantic parity cases.</p>
        <p>Python · GraphQL · RDF · Oxigraph</p>
        <p>
          <a href="https://github.com/ironLegion88/fkg-graphql-layer/tree/sprint-2/cytoscape">Code ↗</a>
        </p>
        <details>
          <summary>Evaluation notes</summary>
          <p>The bundled fixture has 12 matching comparisons out of 14. The two accepted differences concern relationship exposure and inferred class membership. The prototype also has RDF ingestion regression checks.</p>
        </details>
      </td>
      <td width="50%">
        <a href="https://github.com/ironLegion88/yelp-polyglot-ml-pipeline">
          <picture>
            <source media="(prefers-color-scheme: dark)" srcset="./assets/yelp-dark.svg">
            <source media="(prefers-color-scheme: light)" srcset="./assets/yelp-light.svg">
            <img src="./assets/yelp-light.svg" alt="Yelp evaluation. Prediction error examined separately across vote ranges." width="100%">
          </picture>
        </a>
        <h3>Yelp Useful-Vote Prediction</h3>
        <p>XGBoost with review and graph features. Stratified error analysis across vote ranges, with SHAP to examine feature reliance.</p>
        <p>Python · Polars · XGBoost · SHAP</p>
        <p>
          <a href="https://github.com/ironLegion88/yelp-polyglot-ml-pipeline">Code &amp; analysis ↗</a>
        </p>
      </td>
    </tr>
    <tr>
      <td width="50%">
        <a href="https://github.com/ironLegion88/word-games">
          <picture>
            <source media="(prefers-color-scheme: dark)" srcset="./assets/word-games-dark.svg">
            <source media="(prefers-color-scheme: light)" srcset="./assets/word-games-light.svg">
            <img src="./assets/word-games-light.svg" alt="Word Games in Rust. A five-letter word represented as letter tiles." width="100%">
          </picture>
        </a>
        <h3>Word Games in Rust</h3>
        <p>Spelling Bee, Boggle, and Wordle on an arena-backed trie. Differential tests compare optimized solvers against reference implementations.</p>
        <p>Rust · Cargo · Criterion</p>
        <p>
          <a href="https://github.com/ironLegion88/word-games">Code &amp; quick start ↗</a>
        </p>
        <details>
          <summary>Correctness checks</summary>
          <p>The Wordle suite compares feedback implementations across 59,049 guess–target pairs. The trie tests cover physical pruning, free-list reuse, compaction, and randomized reference-model comparisons.</p>
        </details>
      </td>
    </tr>
    <tr>
      <td colspan="2">
        <a href="https://github.com/ironLegion88/IndiSight-Nowcast/tree/feat/data-ingestion">
          <picture>
            <source media="(prefers-color-scheme: dark)" srcset="./assets/indisight-dark.svg">
            <source media="(prefers-color-scheme: light)" srcset="./assets/indisight-light.svg">
            <img src="./assets/indisight-light.svg" alt="IndiSight. District data, SQL retrieval, policy documents, and a benchmark contract." width="100%">
          </picture>
        </a>
        <h3>IndiSight</h3>
        <p>District-level tabular ingestion, PostGIS storage, and an LLM agent with SQL and policy-document retrieval tools. With benchmark checks for required files, metric keys, prediction columns, and JSON object structure.</p>
        <p>Python · PostgreSQL/PostGIS · Streamlit · LLM tooling</p>
        <p>
          <a href="https://github.com/ironLegion88/IndiSight-Nowcast/tree/feat/data-ingestion">Code ↗</a>
        </p>
        <details>
          <summary>Validation details</summary>
          <p>The contract checks for <code>R2</code>, <code>MAE</code>, and <code>RMSE</code> in the metrics object, and <code>district_lgd_code</code>, <code>actual</code>, <code>predicted</code>, and <code>delta</code> in the prediction table. It also checks that the metrics and SHAP files parse as JSON objects.</p>
        </details>
      </td>
    </tr>
  </tbody>
</table>

## More projects

<table width="100%">
  <tbody>
    <tr>
      <td colspan="2">
        <a href="https://disaster-intelligence.streamlit.app/">
          <picture>
            <source media="(prefers-color-scheme: dark)" srcset="./assets/disaster-dark.svg">
            <source media="(prefers-color-scheme: light)" srcset="./assets/disaster-light.svg">
            <img src="./assets/disaster-light.svg" alt="Disaster Intelligence. Comparing coverage of Haiti’s 2021 earthquake and Myanmar’s 2025 earthquake." width="100%">
          </picture>
        </a>
        <h3>Disaster Intelligence Pipeline</h3>
        <p>Collected GDACS reports and built NLP analysis and a Streamlit dashboard to compare news volume, entities, sentiment, and response-timing proxies for two earthquake case studies.</p>
        <p>Python · Pandas · spaCy · Plotly · Streamlit</p>
        <p>
          <a href="https://disaster-intelligence.streamlit.app/">Open dashboard ↗</a> · <a href="https://github.com/ironLegion88/Disaster-Intelligence-Pipeline">Code ↗</a>
        </p>
      </td>
    </tr>
    <tr>
      <td width="50%">
        <a href="https://github.com/ironLegion88/mips-simulator">
          <picture>
            <source media="(prefers-color-scheme: dark)" srcset="./assets/mips-dark.svg">
            <source media="(prefers-color-scheme: light)" srcset="./assets/mips-light.svg">
            <img src="./assets/mips-light.svg" alt="MIPS assembler and simulator. Assembly instructions and register state." width="100%">
          </picture>
        </a>
        <h3>MIPS Assembler &amp; Simulator</h3>
        <p>Two-pass assembly, step execution, and register/memory inspection in a React–Flask interface, with reverse stepping and cache simulation.</p>
        <p>Python · Flask · React · Monaco · pytest</p>
        <p>
          <a href="https://github.com/ironLegion88/mips-simulator">Code ↗</a>
        </p>
      </td>
      <td width="50%">
        <a href="https://github.com/ironLegion88/artemis-captioning">
          <picture>
            <source media="(prefers-color-scheme: dark)" srcset="./assets/artemis-dark.svg">
            <source media="(prefers-color-scheme: light)" srcset="./assets/artemis-light.svg">
            <img src="./assets/artemis-light.svg" alt="ArtEmis image captioning. Artwork, an emotion input, and a captioning model." width="100%">
          </picture>
        </a>
        <h3>ArtEmis Captioning</h3>
        <p>Implemented CNN–LSTM attention and ViT-based captioning models for artwork. Added artwork-level dataset splitting and batch checkpoint evaluation.</p>
        <p>Python · PyTorch · torchvision · NLP</p>
        <p>
          <a href="https://github.com/ironLegion88/artemis-captioning">Code &amp; experiments ↗</a>
        </p>
      </td>
    </tr>
    <tr>
      <td width="50%">
        <a href="https://github.com/Makerspace-Ashoka/DiscProdSheetify">
          <picture>
            <source media="(prefers-color-scheme: dark)" srcset="./assets/discord-dark.svg">
            <source media="(prefers-color-scheme: light)" srcset="./assets/discord-light.svg">
            <img src="./assets/discord-light.svg" alt="Discord product workflow. URLs are extracted, validated, and written to Sheets." width="100%">
          </picture>
        </a>
        <h3>Discord Product Bot</h3>
        <p>Async URL ingestion, Selenium scraping, Gemini-assisted parsing, and Pydantic validation. Writes product records to Google Sheets, deployed with systemd and GitHub Actions.</p>
        <p>Python · asyncio · Gemini · Pydantic</p>
        <p>
          <a href="https://github.com/Makerspace-Ashoka/DiscProdSheetify">DiscProdSheetify code ↗</a>
        </p>
      </td>
      <td width="50%">
        <a href="https://github.com/ironLegion88/library_recommender">
          <picture>
            <source media="(prefers-color-scheme: dark)" srcset="./assets/library-dark.svg">
            <source media="(prefers-color-scheme: light)" srcset="./assets/library-light.svg">
            <img src="./assets/library-light.svg" alt="Library recommendation. A failed search is enriched with corrections and related titles." width="100%">
          </picture>
        </a>
        <h3>Library Recommender</h3>
        <p>Hybrid search recovery using catalogue metadata, circulation signals, and Google Books. Built fuzzy query correction, caching, and a FastAPI service deployed on AWS Lightsail.</p>
        <p>Python · FastAPI · Koha · AWS</p>
        <p>
          <a href="https://koha.ashoka.edu.in/">Library Website ↗</a> · <a href="https://github.com/ironLegion88/library_recommender">Code ↗</a>
        </p>
      </td>
    </tr>
  </tbody>
</table>

## Experience

### SciCommons · Full-stack development intern

<p>
  <em>Current · Prof. Suresh Krishna, McGill</em>
</p>

<ul>
  <li>Submitted two React frontend PRs covering owned-feed discovery, private/unlisted defaults, tag filters, feed configuration, accessible help, and onboarding. Both PRs are open.</li>
  <li>Expanded browser coverage from 24 to 57 tests across keyboard/focus paths, touch layouts, and overflow behavior, tested with Chromium. Also working on a UI/UX redesign.</li>
</ul>

<p>
  <a href="https://feed.scicommons.org/scicommons/default">Public research feed ↗</a>
</p>

### Indian Food Knowledge Graph · Research intern

<p>
  <em>CDSA, Ashoka University · May–Aug 2024 and Jun–Aug 2026</em>
</p>

<p>Contributed to multilingual recipe discovery and knowledge exploration using Next.js, FastAPI, Typesense, LLM query understanding, retrieval, and voice interfaces.</p>

### Makerspace · Flagship project intern

<p>
  <em>Mphasis AI &amp; Applied Tech Lab, Ashoka University · May–Dec 2025</em>
</p>

<p>Built a <a href="https://github.com/Makerspace-Ashoka/DiscProdSheetify">procurement automation bot</a> for the lab, including structured product extraction and Linux service deployment.</p>

### HDFC Library · Software engineering intern

<p>
  <em>Ashoka University · May–Aug 2025</em>
</p>

<p>Built <a href="https://github.com/ironLegion88/library_recommender">search enrichment for Koha</a> using 165K+ catalogue and circulation records, with metadata- and popularity-based ranking.</p>

<details>
  <summary>Teaching, earlier work &amp; robotics</summary>
  <p>
    <strong>Teaching assistant at Ashoka University</strong>
  </p>
  <ul>
    <li>Operating Systems Lab · Current</li>
    <li>Computer Organization and Systems · Jan–May 2025</li>
    <li>Internet of Things, Lodha Genius Programme · Aug–Dec 2025</li>
  </ul>
  <p>
    <strong>Earlier projects</strong>
  </p>
  <ul>
    <li>
      <a href="https://github.com/ironLegion88/media_bias">Media Bias Analysis</a> · Entity-aware sentence sentiment, topic models, and election-news analysis.</li>
    <li>
      <a href="https://github.com/ironLegion88/Autonomous-UAV">Autonomous UAV &amp; Digital Twin</a> · Companion-computer, telemetry, and simulation architecture.</li>
    <li>Micromouse · Q-learning on 20×20 mazes, compared with BFS paths, plus a hardware navigation prototype.</li>
  </ul>
  <p>I’m also interested in the longer-term application of AI safety and auditing to robotics and embedded systems.</p>
</details>

## Tools I work with

<p>
  <strong>Languages</strong>
  <br>Rust · Python · TypeScript · JavaScript · SQL</p>

<p>
  <strong>ML &amp; data</strong>
  <br>PyTorch · scikit-learn · XGBoost · SHAP · Pandas · NumPy · GraphDB · Neo4j · PostgreSQL/PostGIS</p>

<p>
  <strong>Software &amp; verification</strong>
  <br>React · Next.js · FastAPI · Flask · pytest · Cargo · Linux · Docker · GitHub Actions · AWS</p>

## Connect

<p>
  <a href="https://www.linkedin.com/in/sarthak--rathi">LinkedIn ↗</a>
</p>
