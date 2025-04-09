<header>

<!--
  <<< Author notes: Course header >>>
  Include a 1280×640 image, course title in sentence case, and a concise description in emphasis.
  In your repository settings: enable template repository, add your 1280×640 social image, auto delete head branches.
  Add your open source license, GitHub uses MIT license.
-->
<div align="center">
<h1>Awesome Test-time-Scaling in LLMs</h1>
</div>


<p align="center">
  <img src="https://img.shields.io/badge/Contributors-10-red?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/testtimescaling/testtimescaling.github.io?style=for-the-badge&color=blue"/>
  <img src="https://img.shields.io/endpoint?url=https://testtimescaling.github.io/arxiv_citations.json&style=for-the-badge&color=green"/>
</p>

Our repository, **Awesome Test-time-Scaling in LLMs**, gathers available papers on test-time scaling, to our current knowledge. Unlike other repositories that categorize papers, we decompose each paper's contributions based on the taxonomy provided by ["What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models"](https://arxiv.org/abs/2503.24235) facilitating easier understand and comparison for readers.


| Method | What | How → |        |        |        |        |        | Where |
|--------|------|-------|--------|--------|--------|--------|--------|-------|
|        |      | SFT   | RL     | STIMULATION | SEARCH | VERIFICATION | AGGREGATION |
|<li><i><b>Generative language modeling for automated theorem proving</b></i>, Polu et al., <a href="https://arxiv.org/abs/2009.03393" target="_blank"><img src="https://img.shields.io/badge/arXiv-2020.09-red" alt="arXiv Badge"></a></li>|123|123|123|123|123|123|123|123|123|

_Create a site or blog from your GitHub repositories with GitHub Pages._

</header>

<!--
  <<< Author notes: Step 2 >>>
  Start this step by acknowledging the previous step.
  Define terms and link to docs.github.com.
  Historic note: previous version checked for empty pull request, changed to the correct theme `minima`.
-->

## Step 2: Configure your site

_You turned on GitHub Pages! :tada:_

We'll work in a branch, `my-pages`, that I created for you to get this site looking great. :sparkle:

Jekyll uses a file titled `_config.yml` to store settings for your site, your theme, and reusable content like your site title and GitHub handle. You can check out the `_config.yml` file on the **Code** tab of your repository.

We need to use a blog-ready theme. For this activity, we will use a theme named "minima".

### :keyboard: Activity: Configure your site

1. Browse to the `_config.yml` file in the `my-pages` branch.
1. In the upper right corner, open the file editor.
1. Add a `theme:` set to **minima** so it shows in the `_config.yml` file as below:
   ```yml
   theme: minima
   ```
1. (optional) You can modify the other configuration variables such as `title:`, `author:`, and `description:` to further customize your site.
1. Commit your changes.
1. (optional) Create a pull request to view all the changes you'll make throughout this course. Click the **Pull Requests** tab, click **New pull request**, set `base: main` and `compare:my-pages`.
1. Wait about 20 seconds then refresh this page (the one you're following instructions from). [GitHub Actions](https://docs.github.com/en/actions) will automatically update to the next step.

<footer>

<!--
  <<< Author notes: Footer >>>
  Add a link to get support, GitHub status page, code of conduct, license link.
-->

---

Get help: [Post in our discussion board](https://github.com/orgs/skills/discussions/categories/github-pages) &bull; [Review the GitHub status page](https://www.githubstatus.com/)

&copy; 2023 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

</footer>
