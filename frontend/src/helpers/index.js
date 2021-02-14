export default function filterVideoUrlByExtension (value, extension) {
  return `/media/${value.split('.')[0]}.${extension}`
}
