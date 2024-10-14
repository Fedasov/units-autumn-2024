import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';

afterEach(jest.clearAllMocks);

let productWithImg : Product = {
    name: 'product',
    id: 1,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Одежда',
    imgUrl: '/iphone.png'
}

let productWithoutImg : Product = {
    name: 'product',
    id: 2,
    description: 'good',
    price: 1,
    priceSymbol: '$',
    category: 'Одежда',
}

let productAnotherSymbol : Product = {
    name: 'product',
    id: 3,
    description: 'good',
    price: 1,
    priceSymbol: '₽',
    category: 'Одежда',
}

describe('product card test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard key={productWithoutImg.id} {...productWithoutImg}/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly with img', () => {
        const rendered = render(<ProductCard key={productWithImg.id} {...productWithImg}/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('it should be displayed correctly with a different symbol', () => {
        const rendered = render(<ProductCard key={productAnotherSymbol.id} {...productAnotherSymbol}/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});