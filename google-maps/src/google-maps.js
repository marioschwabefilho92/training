import React from 'react'
import { GoogleMap, LoadScript } from '@react-google-maps/api';
import { Marker, InfoWindow } from '@react-google-maps/api';
import { useEffect, useState } from "react";
import { googleMapsApiKey } from "../secrets"

const markerArr = [
  { lat: 17.772, lng: 10.214 },
  { lat: 27.772, lng: 20.214 },
  { lat: 37.772, lng: 30.214 },
];

const containerStyle = {
  width: '1200px',
  height: '800px'
};

const center = {
  lat: -3.745,
  lng: -38.523
};

const position = {
  lat: 37.772,
  lng: 20.214
}

const onLoadMarker = marker => {
  console.log('marker: ', marker)
}

const onLoadWindow = window => {
  console.log('window: ', window)
}


function MyComponent() {

  const [selectedMarkerWindow, setSelectedMarkerWindow] = useState(null);

  function handleClickMarker(position, event) {
    console.log("possiiti");
    console.log(position);
    console.log(event);
    setSelectedMarkerWindow(position);
  }

  return (
    <>
      <LoadScript
        googleMapsApiKey={googleMapsApiKey}
      >
        <GoogleMap
          mapContainerStyle={containerStyle}
          center={center}
          zoom={10}
        >
          {markerArr.map((marker) => (
            <li key={marker.lat}>
              <Marker
                onClick={() => {
                  handleClickMarker(marker);
                }}
                onLoad={onLoadMarker}
                position={marker}
              />
            </li>
          ))}
          {selectedMarkerWindow && (
            <InfoWindow
              onCloseClick={() => {
                setSelectedMarkerWindow(null);
              }}
              position={{
                lat: selectedMarkerWindow.lat,
                lng: selectedMarkerWindow.lng
              }}
            ><h1>Jummmm</h1>
            </InfoWindow>
          )}
        </GoogleMap>
      </LoadScript>
    </>
  )
}

export default React.memo(MyComponent)