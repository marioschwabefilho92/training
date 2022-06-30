import React from 'react';
import { useTranslation } from 'react-i18next';
import { UsingTComponent } from './components/UsingTComponent';
import { UsingTransComponent } from './components/UsingTransComponent';


export default function App() {
  const { i18n } = useTranslation();

  const changeLanguage = (language) => {
    i18n.changeLanguage(language);
  };

  return (
    <div>
      <div>
        <h1>Buttons used to change language de and en</h1>
        <button type="button" onClick={() => changeLanguage('de')}>
          de
        </button>
        <button type="button" onClick={() => changeLanguage('en')}>
          en
        </button>
      </div>
      <div>
        <h1>Here 2 types of components using different load methods for translation</h1>
        <UsingTComponent />
        <UsingTransComponent />
      </div>
    </div>
  );
}