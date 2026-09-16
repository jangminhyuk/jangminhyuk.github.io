Personal website: https://jangminhyuk.github.io/

## Updating content

- _data/research.yml is the shared publication record. It supplies titles, author lists, status, paper links, and media for both the homepage and /publications/.
- Set featured: true to show a research entry with its figure or video on the homepage.
- _portfolio/ contains detail pages. A research_id connects a page to its publication record and keeps it out of the engineering project listing.
- Engineering projects without a research_id appear at /portfolio/. Use featured_engineering: true and home_order to select and order homepage projects. The card_video and card_image fields specify an inline MP4 and its poster; card_* fields supply the text.
- An optional card_gallery adds supporting media to a homepage project. Each entry has image, alt, and caption fields, plus video for a clip.
- _pages/about.md contains the introduction, background, and homepage sections.
- The current CV is files/Minhyuk_Jang_CV.pdf.

## Design

The updated pages use _layouts/research-site.html, assets/css/research.css, and assets/js/research.js. Existing project URLs are preserved. Legacy template pages still use the original Academic Pages layouts.

Research previews use compressed, muted MP4 clips and poster images. Videos play only while visible; reduced-motion and data-saving preferences disable automatic playback. Visitors can pause previews globally or use each video's native controls.

## Local preview

Run bundle install if needed, then:

    bundle exec jekyll serve --config _config.yml,_config.dev.yml --port 4173

Open http://localhost:4173. On Windows, run from a normal user terminal if a restricted environment cannot read the parent directory of the Sass sources.

After a build, check local links, media, and page headings:

    python scripts/check_site.py

## Reference files

Keep original manuscripts and design references outside this repository. _reference/ and website_reference/ are also ignored and excluded from builds as a safeguard. assets/research/ and assets/projects/ contain selected web-ready media intended for the site; review those assets before publishing. The reference PDFs are not copied into the website.

Pushing to master triggers the existing GitHub Pages deployment.
