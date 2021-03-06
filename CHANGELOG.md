# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

<!--
   PRs should document their user-visible changes (if any) in the
   Unreleased section, uncommenting the header as necessary.
-->

<!-- ## Unreleased -->
<!-- ### Changed -->
<!-- ### Added -->
<!-- ### Removed -->
<!-- ### Fixed -->
<!-- ## Unreleased -->
<!-- ### Changed -->

## [0.7.1] - 2020-02-22

* channelstream-utils can now generate config out of ENV vars
* add option to use different signature checkers
* added more tests

## [0.7.0] - 2019-05-18
### Changed
* Logout and api-explorer links in admin panel
* Persist auth cookie for admin panel

## [0.7.0rc1] - 2019-05-12
### Added
* `channelstream_utils` command, right now it can create fresh config INI files
### Removed
* [breaking] dropped six compat layer
* [breaking] test only in python 3.6+
* [breaking] Allow configuration only from ini files, drop all other arguments from CLI
### Changed
* Admin views can also be accessed when authenticating via API keys
* Updated frontend code to support ESM browsers by default, fallback to ES5 browsers optionally
* Depend on pyramid_apispec 0.3.3
* /api-explorer is now only accessible for admin users

## [0.6.14] - 2019-02-09
### Changed
* Pinned Marshmallow version to <3.0.0
* Bumped pyramid_apispec

## [0.6.13] - 2019-02-07
### Changed
* AuthTkt instead of basic auth, introduces optional `cookie_secret`
* Used lit-element 2.0.1 for components
### Fixed
* changed garbage collection and hearbeat handling that should end with smaller callstacks
* fixed a heartbeat check that could result in greenlets run forever

## [0.6.12] - 2019-02-05
### Added
* `enforce_https` config option forces the servers to reject non-ssl requests
* `http_scheme` config option can be used to enforce HTTPS urls if proper proxy headers are missing
* `/admin/debug` route for printing out greenlets
### Removed
* JS Client code was moved to npm and separate repository
### Changed
* Moved to lit-element 2.0.0rc5

## [0.6.11] - 2019-01-31
### Changed
*  Depends on pyramid_apispec==0.3.1


## [0.6.10] - 2018-11-08
### Changed
*  Depends on pyramid_apispec==0.3.0


## [0.6.9] - 2018-11-02
### Added
* Request validation with Marshmallow schemas
* API Explorer under /api-explorer
* edit and delete message API's
### Changed
*  **[breaking] 0.6 BRANCH IS THE LAST RELEASE THAT SUPPORTS PYTHON OLDER THAN 3.6**
* Demos are now standalone applications
* Uses itsdangerous 1.1.0 for signing, to support 0.24 version additional
  config option `validate_requests` to allow disabling timestamp checks
