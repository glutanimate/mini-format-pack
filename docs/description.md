This is a quick stripped-down version of Stefan van den Akker's [Power Format Pack add-on](https://ankiweb.net/shared/info/162313389) that is designed to work with Anki 2.1. It's only meant as a holdover until someone finds the time to port PFP in its entirety, or until similar features arrive in Anki itself. Please don't expect any further major additions like markdown support, etc.


**SCREENSHOT**

![](https://raw.githubusercontent.com/glutanimate/mini-format-pack/master/screenshots/main.png)

**CURRENT FEATURE-SET**

- Highlight text
- Insert code block
- Insert horizontal line
- Toggle unordered list
- Toggle ordered list
- Indent selection
- Outdent selection
- Alignment buttons

**COMPATIBILITY**

As Anki 2.1 is still being tested it is possible that a future development release will break 2.1 compatibility. **Please do not report issues in the review section below**. Instead, please report all issues you encounter on [GitHub](https://github.com/glutanimate/mini-format-pack/issues).


**CONFIGURATION**

The add-on offers some limited configuration capabilities, but they are not as fleshed out nor as user-friendly as PFP. You will have to use Anki 2.1's built-in config manager to update the config dictionary (Tools → Add-ons → Select Mini Format Pack → Click configure). 

The properties  you can modify include:

- `hotkey` and `tooltip` of each action
- order of actions (by shifting the `{}`-enclosed button definitions around)
- available actions (by deleting any of the `{}`-enclosed button definitions)

Your changes will be applied once you restart your editor window (if running). Please do not change the '`name`' property, as this is used to assign the corresponding button to the function it calls.

**CHANGELOG**

2018-07-18: **v0.1.0** – Initial release

**SUPPORT**

I can only reply to your reviews in a limited fashion, so this is not a good way to report or troubleshoot issues. Instead, please report all issues you encounter either by creating a bug report on [GitHub](https://github.com/glutanimate/mini-format-pack/issues), or by posting a new thread on the [Anki add-on support forums](https://anki.tenderapp.com/discussions/add-ons). Please make sure to include the name of the affected add-on in your report title when you do so.

**CREDITS AND LICENSE**

*Copyright(c) 2014-2018 [Stefan van den Akker](https://relentlesscoding.com/)*
*Copyright(c) 2017-2018 [Damien Elmes](http://ichi2.net/contact.html)*
*Copyright (c) 2018 [Glutanimate](https://glutanimate.com/)*

*Mini Format pack* is based on [*Power Format Pack*](https://github.com/Neftas/supplementary-buttons-anki) by [Stefan van den Akker](https://github.com/Neftas). All credit for the original idea and implementation goes to him. I would like to express my heartfelt gratitude for all of what he has done for the Anki community over the years. PFP was one of the projects that originally inspired me to go into add-on development. Thank you for that, Stefan!

Licensed under the [GNU AGPLv3](https://www.gnu.org/licenses/agpl.html). The code for this add-on is available on [![GitHub icon](https://glutanimate.com/logos/github.svg) GitHub](https://github.com/glutanimate/mini-format-pack).

**MORE RESOURCES**

A lot of my add-ons were commissioned by other Anki users. Please feel free to reach out to me if you would like to hire my services for any Anki-related development work (writing an add-on for you, converting existing ones to Anki 2.1, implementing a specific feature): ![Email icon](https://glutanimate.com/logos/email.svg) <em>ankiglutanimate [αt] gmail .com</em>. 

Want to stay up-to-date with my latest add-on releases and updates? Make sure to follow me on Twitter: [![Twitter bird](https://glutanimate.com/logos/twitter.svg)@Glutanimate](https://twitter.com/glutanimate)

New to Anki? Feel free to check out my YouTube channel where I post weekly tutorials on Anki add-ons and related topics: [![YouTube playbutton](https://glutanimate.com/logos/youtube.svg) / Glutanimate](https://www.youtube.com/c/glutanimate)

**SUPPORT MY WORK**

Writing, supporting, and maintaining Anki add-ons like this takes a lot of time and effort. If *Mini Format Pack* or any of my other add-ons has been a valuable asset in your studies, please consider **buying me a coffee**:

<a href="https://www.buymeacoffee.com/glutanimate" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

Each and every contribution is greatly appreciated and will help me maintain and improve my add-ons as time goes by!
