import { useTranslation } from 'react-i18next';

export function UsingTComponent() {
    const { t } = useTranslation();

    return (
        <>
            <div>
                {t('simple.text1')}
            </div>
            <div>
                {t('simple.text2')}
            </div>
            <div>
                {t('components.UsingTransComponent.title')}
            </div>
        </>
    );
}