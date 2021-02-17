function getVideoUrl (path) {
  if (path) {
    return `/media/${path}`
  }
  return ''
}

function getVideoMIMETypeFromUrl (url) {
  if (typeof url === 'string') {
    const arr = url.split('.')
    const extension = arr[arr.length - 1]
    return `video/${extension}`
  }
  return 'video/mp4'
}

function filterDateFormat (value) {
  const language = window.navigator.language
  const arr = value.split('-')
  if (language === 'ru-RU') {
    return `${arr[2]}.${arr[1]}.${arr[0]}`
  } else if (language === 'en-US') {
    return `${arr[1]}/${arr[2]}/${arr[0]}`
  } else {
    return `${arr[2]}/${arr[1]}/${arr[0]}`
  }
}

export { getVideoUrl, getVideoMIMETypeFromUrl, filterDateFormat }
