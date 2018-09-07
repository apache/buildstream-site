This is the repository that host the content related with the BuildStream
website. The website is available at <https://buildstream.build>.

## Building locally

To work locally with this project, you'll have to follow the steps below:

1. Fork, clone or download this project
1. [Install][pelican-install] Pelican
1. Generate the website: `make html`
1. Preview your project: `make serve`
1. Add content

## Let's Encrypt certificate renewal

The website deployed by this repo supports encrypted communication through
HTTPS using a TLS digital certificate provided by
[Let's Encrypt][lets-encrypt].

These certificates have a validity of three months and thus need to be
periodically renewed. In order to do so, follow these steps.

Clone and use the [Certbot][certboot] tool to generate a new
certificate:

```
git clone https://github.com/certbot/certbot
cd certbot
./letsencrypt-auto certonly -a manual -d buildstream.build -d www.buildstream.build
```

Do not press `enter` yet. On another terminal, follow the instructions
and add a new challenge file with the filename specified to the
`content/.well-known/acme-challenge` directory with the contents also
specified.

Redeploy the website with new file:

```
git add content/.well-known/acme-challenge/
git commit -m "Update Let's Encrypt ACME challenge"
git push origin master
```

After the CI pipeline finishes and the website is redeployed, go back to
the first terminal and press `enter`. This will generate new
`fullchain.pem` and `privkey.pem` files.

Finally, go to domain settings [page][buildstream.build-settings] and
replace _Certificate (PEM)_ with updated `fullchain.pem` and
_Key (PEM)_ with updated `privkey.pem`. Do the same for the for the
subdomain on the settings [page][www.buildstream.build-settings].

Test the new certificate by accessing <https://buildstream.build> and
verifying that no warnings are shown regarding the certificate.

[pelican-install]: http://docs.getpelican.com/en/3.6.3/install.html
[lets-encrypt]: https://letsencrypt.org/
[certboot]: https://certbot.eff.org/
[buildstream.build-settings]: https://gitlab.com/BuildStream/website/pages/domains/buildstream.build/edit
[www.buildstream.build-settings]: https://gitlab.com/BuildStream/website/pages/domains/wwww.buildstream.build/edit
