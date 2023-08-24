import { Trans } from 'react-i18next';

export function UsingTransComponent() {
    return (
        <>
            <div>
                <Trans i18nKey="simple.text1" />
            </div>
            <div>
                <Trans i18nKey="simple.text2" />
            </div>
            <div>
                <Trans i18nKey="components.UsingTransComponent.title" />
            </div>
        </>
    );
}