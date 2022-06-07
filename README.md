# Diversiformer

_Work in progress._

Language model for inclusive language in German, fine-tuned on [mT5](https://arxiv.org/abs/2010.11934).

Pre-trained model to be released later in 2022.

## Tasks

- **DETECT**: Recognizes instances of the generic masculine, and of other exclusive language. To do.
- **SUGGEST**: Suggest inclusive alternatives to masculine and exclusive words. To do.
- **REPLACE**: Replace one phrase by another, while preserving grammatical coherence. Work in progress.

  - ▶️ `Ersetze "Schüler" durch "Schülerin oder Schüler": Die Schüler kamen zu spät.`

    ◀️ `Die Schülerinnen und Schüler kamen zu spät.`

  - ▶️ `Ersetze "Lehrer" durch "Kollegium": Die wartenden Lehrer wunderten sich.`

    ◀️ `Das wartende Kollegium wunderte sich.`

## Dev ideas

- Use classifier to filter out training data of low quality? (~adversarial approach)
- Use subtrees of replaced words (and dependent verbs) instead of whole sentences.

## License

Diversiformer. Transformer model for inclusive language.

Copyright (C) 2022 [Diversifix e. V.](mailto:vorstand@diversifix.org)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
