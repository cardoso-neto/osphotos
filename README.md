# osphotos
Open Source Photos app.

OSPhostos is a metadata editor that enables you to share an image's (or a whole library of images') metadata with friends and with anyone via the internet.

It defines a standard data transfer format for JSONs containing information about an image to be shared with all the standard camera tags preserved as well.

Most importantly:
- People on a photo;
- Arbitrary tags about the image;
- Date taken;
- Camera used and its settings.

The basic plan is for this to replace Google Photos as the best "image indexer" app.

### Roadmap

- Define common data format.
- Create an API that writes to that common format.
- Feature: Merge different libraries together. Needs discussion on how to handle conflicts.
- Semantic stuff: enable users to autodetect faces, auto-generate tags, auto-group similar photos, etc. 

See [queries.md](./design-docs/queries.md) to get an idea of what sort of use cases this is intended to attend.
