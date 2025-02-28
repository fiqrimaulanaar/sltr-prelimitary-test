# Build Image

`docker build -t testing/welcome .`

## Build image untuk di push ke registry GitHub Packages
`docker build -t ghcr.io/fiqrimaulanaar/testing/welcome .`

# Run Image
`docker run -p 8000:5000 testing/welcome`

## Run image menggunakan image yang ada di registry GitHub Packages
`docker run -p 8000:5000 ghcr.io/fiqrimaulanaar/testing/welcome`