import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Categories } from './Categories';

afterEach(jest.clearAllMocks);

describe('test for categories', () => {
    it('should render correctly', () => {
        const rendered = render(<Categories selectedCategories={[]} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('test for adding the class of the selected icon', () => {
        const rendered = render(<Categories selectedCategories={['Одежда']} />);

        expect(rendered.getByText('Одежда')).toHaveClass('categories__badge_selected');
        expect(rendered.getByText('Электроника')).not.toHaveClass('categories__badge_selected');
        expect(rendered.getByText('Для дома')).not.toHaveClass('categories__badge_selected');
    });

    it('callback test when clicking on a category', () => {
        const onCategoryClick = jest.fn();
        const rendered = render(
            <Categories
                selectedCategories={[]}
                onCategoryClick={onCategoryClick}
            />
        );
        expect(onCategoryClick).toHaveBeenCalledTimes(0);
        fireEvent.click(rendered.getByText('Одежда'));
        expect(onCategoryClick).toHaveBeenCalledTimes(1);
    });
});
